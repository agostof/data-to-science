import { useState } from 'react';
import { TrashIcon } from '@heroicons/react/24/outline';

import { Button } from './Buttons';
import Modal from './Modal';
import { ConfirmationPopup } from './ConfirmationPopup';

type ConfirmationModal = {
  btnName: string;
  btnType?: string;
  confirmText: string;
  content: string;
  onConfirm: () => void;
  rejectText: string;
  title: string;
};

export default function ConfirmationModal({
  btnName,
  btnType = 'normal',
  confirmText,
  content,
  onConfirm,
  rejectText,
  title,
}: ConfirmationModal) {
  const [open, setOpen] = useState(false);

  return (
    <div>
      {btnType === 'normal' && (
        <Button type="button" size="sm" onClick={() => setOpen(true)}>
          {btnName}
        </Button>
      )}
      {btnType === 'trashIcon' && (
        <button type="button" onClick={() => setOpen(true)}>
          <span className="sr-only">Remove</span>
          <TrashIcon className="w-4 h-4" />
        </button>
      )}
      <Modal open={open} setOpen={setOpen}>
        <ConfirmationPopup
          title={title}
          content={content}
          confirmText={confirmText}
          rejectText={rejectText}
          setOpen={setOpen}
          onConfirm={onConfirm}
        />
      </Modal>
    </div>
  );
}
