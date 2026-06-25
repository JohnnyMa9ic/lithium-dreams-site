export type StatusTag =
  | 'OPEN'
  | 'FLICKERING'
  | 'STAFF ONLY'
  | 'UNDER REPAIR'
  | 'BY APPOINTMENT'
  | 'RESTRICTED'
  | 'COMING SOON'
  | 'ARCHIVED'
  | 'UNSTABLE';

export interface District {
  title: string;
  description: string;
  status: StatusTag;
  href: string;
  icon: string;
  microcopy: string;
  inNav: boolean;
}

export const districts: District[] = [
  {
    title: 'Gift Shop',
    description: 'Souvenirs, field notes, stickers, and objects we are legally allowed to sell.',
    status: 'OPEN',
    href: '/gift-shop',
    icon: '🎪',
    microcopy: 'No refunds after portal exposure.',
    inNav: true,
  },
  {
    title: 'Arcade',
    description: 'Project cabinets, experimental builds, and things that almost work.',
    status: 'FLICKERING',
    href: '/arcade',
    icon: '🕹',
    microcopy: 'Please do not unplug the cabinet in the corner.',
    inNav: true,
  },
  {
    title: 'Museum',
    description: 'Curated case files, lore fragments, and a timeline we are still reconstructing.',
    status: 'OPEN',
    href: '/museum',
    icon: '🏺',
    microcopy: 'Please do not tap the glass.',
    inNav: true,
  },
  {
    title: 'Fortune Emporium',
    description: "Bob's cabinet. Insert a question. Results are not guaranteed but are usually interesting.",
    status: 'UNSTABLE',
    href: '/fortune',
    icon: '🔮',
    microcopy: 'Temporarily sentient. Bob says this is probably fine.',
    inNav: true,
  },
  {
    title: 'Snack Counter',
    description: 'Temporarily unmanned. The register is still running.',
    status: 'UNDER REPAIR',
    href: '#',
    icon: '🍿',
    microcopy: 'Maintenance has already been notified.',
    inNav: false,
  },
  {
    title: 'Lost & Found',
    description: 'Something has already been turned in on your behalf.',
    status: 'OPEN',
    href: '#',
    icon: '📦',
    microcopy: 'Extraterrestrial parking has moved behind the chapel.',
    inNav: false,
  },
  {
    title: 'Wedding Chapel',
    description: 'Open Tuesdays and Fridays. Do not ask about the back room.',
    status: 'BY APPOINTMENT',
    href: '/chapel',
    icon: '⛪',
    microcopy: 'Reflections may desynchronize during electrical storms.',
    inNav: true,
  },
  {
    title: 'Employees Only',
    description: 'Authorized staff, maintenance personnel, cryptids with valid badges, and Bob.',
    status: 'RESTRICTED',
    href: '/employees-only',
    icon: '🔒',
    microcopy: 'Please do not feed the groundskeeper.',
    inNav: true,
  },
];
